document.addEventListener("DOMContentLoaded", function() {
  var metaDescriptionField = document.querySelector('#id_meta_description');
  var charCountContainer = document.createElement('p');
  charCountContainer.className = "meta-description-char-count";
  metaDescriptionField.parentNode.insertBefore(charCountContainer, metaDescriptionField.nextSibling);
  var maxChars = 160;

  function updateCharCount() {
      var charCount = metaDescriptionField.value.length;
      charCountContainer.textContent = charCount + ' of ' + maxChars + ' символов';
  }

  metaDescriptionField.addEventListener('keyup', updateCharCount);
  updateCharCount();
});
document.addEventListener("DOMContentLoaded", function() {
  var metaDescriptionField = document.querySelector('#id_meta_title');
  var charCountContainer = document.createElement('p');
  charCountContainer.className = "meta_title-char-count";
  metaDescriptionField.parentNode.insertBefore(charCountContainer, metaDescriptionField.nextSibling);
  var maxChars = 60;

  function updateCharCount() {
      var charCount = metaDescriptionField.value.length;
      charCountContainer.textContent = charCount + ' of ' + maxChars + ' символов';
  }

  metaDescriptionField.addEventListener('keyup', updateCharCount);
  updateCharCount();
});
