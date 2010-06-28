// Author: Aziz
// License: zlib/libpng

function COEM_enableSplitting(checkbox)
{
  if (!window.$) return;
  var textarea = $('#postmodify textarea.editor');
  var handleEvent = COEM_enableSplitting.handler;
  var un_bind = checkbox.checked?'bind':'unbind';
  textarea[un_bind]('keyup', handleEvent)
          [un_bind]('click', handleEvent);
}

COEM_enableSplitting.handler = function handleEvent(e) {
    e = e || window.event;
    if (e.keyCode == 13 && e.shiftKey || e.ctrlKey && e.button == 0)
      COEM_splitTags();
}

function COEM_parseTags(text, endPos)
{ //         [    name    attrs  |  /name     ]
  var rx = /\[(?:([a-z]+)([^\]]*)|(\/[a-z]+))\]/gi;
  var tagStack = [];
  text = text.slice(0, endPos); // "m.index < endPos" doesn't seem to work.
  while ((m = rx.exec(text)) /*&& m.index < endPos*/)
    if (m[3]) // [/tagName]
      tagStack.pop()
    else
      tagStack.push({"name":m[1], "attributes":m[2]}); // [tagName]
  return tagStack;
}

function COEM_splitTags()
{ // Splits tags at the current cursor position.
  var form = document.getElementById("postmodify");
  var textarea = form.elements.namedItem("message");

  var string = textarea.value;
  var endPos = Math.min(textarea.selectionStart, string.length)
  var tagStack = COEM_parseTags(string, endPos);

  if (tagStack.length == 0)
    return;

  var tagText = "";

  // Traverse in reverse and append closing tags.
  for (var i = tagStack.length-1; i >= 0; i--)
    tagText += '[/' + tagStack[i].name + "]\n";

  var newCaretPos = tagText.length + tagStack.length;

  for (var i = 0; i < tagStack.length; i++)
    if (tag = tagStack[i])
      tagText += '\n[' + tag.name + tag.attributes + "]";

  COEM_replaceText(tagText, newCaretPos, textarea);
  return false;
}

function COEM_replaceText(text, textCaretPos, textarea)
{
  function setCaretToPos(input, pos) {
    input.setSelectionRange(pos, pos);
  }

  function getSelectionStart(o) {
    if (o.createTextRange) {
      var r = document.selection.createRange().duplicate()
      r.moveEnd('character', o.value.length)
      return (r.text == '') ? o.value.length : o.value.lastIndexOf(r.text);
    }
    return o.selectionStart
  }

  // Attempt to create a text range (IE).
  if (typeof(textarea.caretPos) != "undefined" && textarea.createTextRange)
  {
    var caretPos = textarea.caretPos;
    var selStart = getSelectionStart(textarea); //textarea.selectionStart;
    caretPos.text = caretPos.text.slice(-1) == ' ' ? text + ' ' : text;
    setCaretToPos(textarea, selStart + textCaretPos);
  }
  // Mozilla text range replace.
  else if (typeof(textarea.selectionStart) != "undefined")
  {
    var selStart = textarea.selectionStart;
    var begin = textarea.value.substr(0, selStart);
    var end = textarea.value.substr(textarea.selectionEnd);
    var scrollPos = textarea.scrollTop;

    textarea.value = begin + text + end;

    if (textarea.setSelectionRange)
    {
      textarea.focus();
      var newCaretPos = begin.length + textCaretPos - 1;
      textarea.setSelectionRange(newCaretPos, newCaretPos);
    }
    textarea.scrollTop = scrollPos;
  }
  // Just put it on the end.
  else
  {
    textarea.value += text;
    textarea.focus(textarea.value.length - 1);
  }
}
