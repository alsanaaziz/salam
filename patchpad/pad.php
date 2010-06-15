<?php

$base_urls = array(
  'github' => 'http://github.com/alsanaaziz/salam/raw/master/',
  'books' => 'http://github.com/alsanaaziz/salam/raw/master/books/',
  'subs' => 'http://github.com/alsanaaziz/salam/raw/master/subtitles/',
  '' => '',
);
$cache_dir = 'cache/';

$doc = $_GET['doc'];
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
  $msg = $_POST['msg'];
  $nick = $_POST['nick'];
  $to = 'alsana.aziz+patchpad@gmail.com';
  $subject = 'Patch: '.$doc; // TODO: only append document name?
  $message = "By: $nick\n\nMessage:\n$msg\n\nPatch:\n\n" . $patch;
  $headers = "From: patchpad@councilofexmuslims.com";
  $success = mail($to, $subject, $message, $headers);
  echo $success;
  die();
}

// %20 = escape space.
$doc_url = $base_url . str_replace(' ', '%20', $doc);

$fname = "$cache_dir$base_url_key:" . str_replace('/', '_', $doc) . '.cache';
$fetch_from_web = !file_exists($fname);
$doc_contents = '';

if ($fetch_from_web)
{
  $doc_contents = @file_get_contents($doc_url);
  if ($doc_contents === false)
    die('<b>Error:</b> Couldn\'t fetch "'.$doc_url.'".');
  $f = fopen($fname, "w");
  fwrite($f, $doc_contents);
  fclose($f);
}
else
  $doc_contents = file_get_contents($fname);

// Finally include the template:
include "./pad.tpl";
?>
