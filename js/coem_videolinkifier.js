// Author: Aziz
// License: zlib/libpng

function getSettingsLink()
{
  var storage = window.localStorage;
  if (!storage) return null;
  var tag = $('<span> (<a href="">Settings</a><span>Embedding: <select></select>\
</span>)</span>'), opts = [0,5,10,20,35,1000];
  tag.find(">a").click(function _(e){
    e.preventDefault();
    var $t = $(this).text("").unbind("click", _);
    if (!storage)
      $t.after(' “Web Storage” is unsupported by your browser');
    else
      $t.next().show();
  });
  tag.find(">span").hide();
  var sel = tag.find("select").change(function(){
    storage.embed_nr = opts[$(this).find("option:selected")[0].value];
  });
  var nr = Number(storage.embed_nr || 5), opt = $.inArray(nr, opts);
  $(['Only preview images','Max. 5/page','Max. 10','Max. 20','Max. 35','All'])
    .each(function(i, e){sel.append('<option value="'+i+'"'+(i==opt?' selected="true"':"")+'>'+e+'</option>')});
  tag.max = nr;
  return tag;
}

$(function linkifyVideos() {
  var domain_rx = /([\w-]+\.\w+)\/(.+)$/;
  var embed_html = '<embed width="450px" height="360px" allowscriptaccess="never"\
 allowfullscreen="true" quality="high" wmode="transparent" src="{src}"\
 type="application/x-shockwave-flash"/>';
  function getEmbed(s){return embed_html.replace('{src}',s)}
  function showFlash(tag, eURL){$(tag).replaceWith(getEmbed(eURL))}
  function getIMG(a, src, eURL, eURLa)
  {
    return $('<a href="'+a.href+'"><img alt="Preview image" '+
      'title="Click to play or double-click to load." src="'+src+'"/></a>')
      .dblclick(function(e) {
      e.preventDefault();
      clearTimeout(this.tID); // Prevent single click.
      showFlash(this, eURL);
    }).click(function(e) {
      e.preventDefault();
      t = this;
      t.tID = setTimeout(function(){showFlash(t, eURLa)}, 200);
    });
  }
  function embedOrIMG(emb, a, src, eURL, eURLa)
  { eURL='http://'+eURL; return emb ? getEmbed(eURL) : getIMG(a, 'http://'+src, eURL, 'http://'+eURLa); }

  var handlers = {
  'youtube.com' : function(path, a, emb) {
    var vID = path.match(/\bv[=/]([^&#?$]+)/i) || path.match(/#p\/(?:a\/)?[uf]\/\d+\/([^?$]+)/i);
    if (!vID || !(vID = vID[1])) return;
    var embedURL = 'youtube.com/v/'+vID,
      tag = embedOrIMG(emb, a, 'img.youtube.com/vi/'+vID+'/0.jpg',
      embedURL, embedURL+'&amp;autoplay=1');
    return ["YouTube Video:", tag];
  },
  'google.com' : function(path, a, emb) {
    var vID = path.match(/\bdocid=([^&#$]+)/i);
    if (!vID || !(vID = vID[1])) return;
    var embedURL = 'video.google.com/googleplayer.swf?fs=true&amp;docid='+vID,
      tag = embedOrIMG(emb, a, 'www.google.com/images/video_logo.png', //gvt0
      embedURL, embedURL+'&amp;autoplay=1');
    return ["Google Video:", tag];
  },
  'vimeo.com' : function(path, a, emb) {
    var vID = path.match(/^(\d+)/i);
    if (!vID || !(vID = vID[1])) return;
    var embedURL = 'vimeo.com/moogaloop.swf?clip_id='+vID,
      tag = embedOrIMG(emb, a, 'assets.vimeo.com/images/logo_vimeo_land.png',
      embedURL, embedURL+'&amp;autoplay=1');
    return ["Vimeo Video:", tag];
  }
  };
  //handlers['google.co.uk'] = handlers['google.com'];

  var links = $('#quickModForm a'); // Get the links in the postings.
  var settings = getSettingsLink() || $("");
  var embed_nr = window.localStorage ? localStorage.embed_nr : 5;
  for (var i=links.length-1; i > -1; i--)
  {
    var tag = links[i];
    if ("quote;signature".indexOf(tag.parentNode.className) != -1)
      continue; // Ignore in quotes.
    var text = tag.innerText || tag.textContent || "";
    if (tag.href == "" || tag.href.indexOf(text) == -1)
      continue; // No href attr, or inner text not equal to href attr.
    if ((m = tag.href.match(domain_rx)) && // Get domain.
      (handler = handlers[m[1]]) && // Is there a handler for this domain?
      (args = handler(m[2], tag, embed_nr > 0))) { // Call the handler.
      --embed_nr;
      $(tag).text(args[0]).before("<p></p>").after(settings.clone(true), "<br/>", args[1], "<br/>");
    }
  }
});
