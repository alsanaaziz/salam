<?php
$githubcom = 'http://github.com/alsanaaziz/salam/raw/master/';
$base_urls = array(
  'github' => $githubcom,
  'books' => $githubcom.'books/',
  'subs' => $githubcom.'subtitles/',
  '' => $githubcom,
);
$cache_dir = 'cache/';

$doc = $_GET['doc'];
$clear_cache = $_GET['cache'] == 'clear';
$doc = $doc ? $doc : 'books:My_Ordeal_With_The_Quran.tex';

$parts = explode(':', $doc, 2);
if (count($parts) == 1)
  $parts = array('', $parts[0]);
$base_url_key = $parts[0];
$base_url = $base_urls[$base_url_key];
$doc = $parts[1];

$patch = $_POST['patch'];
if ($patch)
{
  require_once 'lib/swift_required.php';
  $msg = $_POST['msg'];
  $nick = $_POST['nick'];
  $to = 'alsana.aziz+patchpad@gmail.com';
  $subject = 'Patch: '.$doc; // TODO: only append document name?
  $message = "By: $nick\n\nMessage:\n$msg";

  // Create the Transport.
  $transport = Swift_MailTransport::newInstance();
  // Create the Mailer using your created Transport.
  $mailer = Swift_Mailer::newInstance($transport);
  // Create a message.
  $message = Swift_Message::newInstance($subject)
    ->setFrom(array('patchpad@councilofexmuslims.com' => 'PatchPad'))
    ->setTo(array($to))
    ->setBody($message)
    ->attach(Swift_Attachment::newInstance($patch, 'a.patch', 'text/x-diff'));
  //Send the message
  $result = $mailer->send($message);
  // $result = $mailer->batchSend($message);
  echo $result;
  die();
// Obsolete:
//   $headers = "From: patchpad@councilofexmuslims.com";
//   $success = mail($to, $subject, $message, $headers);
}

// $cache_life in seconds.
// if (!file_exists($cache_file) or (time() - filemtime($cache_file) >= $cache_life))

function fetch_from_web($fname, $clear_cache)
{ /// Returns true if the file should be fetched from the web.
  return !file_exists($fname) or $clear_cache;
}

// %20 = escape space.
$doc_url = $base_url . str_replace(' ', '%20', $doc);

$fname = "$cache_dir$base_url_key:" . str_replace('/', '_', $doc) . '.cache';
$doc_contents = '';

if (fetch_from_web($fname, $clear_cache))
{
  $doc_contents = @file_get_contents($doc_url);
  if ($doc_contents === false)
    die('<b>Error:</b> Couldn\'t fetch "'.$doc_url.'".');
  $f = fopen($fname, 'w');
  fwrite($f, $doc_contents);
  fclose($f);
}
else
  $doc_contents = file_get_contents($fname);

// Finally include the template:
include "./pad.tpl";
?>
