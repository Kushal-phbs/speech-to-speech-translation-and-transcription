"use strict";

const directionSelect = document.querySelector("#direction");
const sourceLanguage = document.querySelector("#source-language");
const targetLanguage = document.querySelector("#target-language");
const sourcePill = document.querySelector("#source-pill");
const targetPill = document.querySelector("#target-pill");
const sourceText = document.querySelector("#source-text");
const characterCount = document.querySelector("#character-count");

const directions = {
  "en-to-hi": {
    source: "English",
    target: "हिन्दी",
    targetCode: "hi",
    sourcePill: "ENGLISH",
    targetPill: "हिन्दी · HINDI",
    placeholder: "Type something in English…",
  },
  "hi-to-en": {
    source: "हिन्दी",
    target: "English",
    targetCode: "en",
    sourcePill: "हिन्दी · HINDI",
    targetPill: "ENGLISH",
    placeholder: "हिन्दी में कुछ लिखें…",
  },
};

function updateDirection() {
  const direction = directions[directionSelect.value];
  sourceLanguage.textContent = direction.source;
  targetLanguage.textContent = direction.target;
  targetLanguage.lang = direction.targetCode;
  sourcePill.textContent = direction.sourcePill;
  targetPill.textContent = direction.targetPill;
  sourceText.placeholder = direction.placeholder;
}

directionSelect.addEventListener("change", updateDirection);
sourceText.addEventListener("input", () => {
  characterCount.textContent = `${sourceText.value.length} / ${sourceText.maxLength}`;
});
