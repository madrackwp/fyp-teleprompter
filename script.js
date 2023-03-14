const startBtn = document.querySelector("#startBtn");
const stopBtn = document.querySelector("#stopBtn");
const result = document.querySelector("#display");
var SpeechRecognition = SpeechRecognition || webkitSpeechRecognition;
var SpeechGrammarList = SpeechGrammarList || window.webkitSpeechGrammarList;
var SpeechRecognitionEvent = SpeechRecognitionEvent || webkitSpeechRecognitionEvent;

var recognition = new SpeechRecognition();

// console.log(recognition);

var colors = [
  "aqua",
  "azure",
  "beige",
  "bisque",
  "black",
  "blue",
  "brown",
  "chocolate",
  "coral",
  "crimson",
  "cyan",
  "fuchsia",
  "ghostwhite",
  "gold",
  "goldenrod",
  "gray",
  "green",
  "indigo",
  "ivory",
  "khaki",
  "lavender",
  "lime",
  "linen",
  "magenta",
  "maroon",
  "moccasin",
  "navy",
  "olive",
  "orange",
  "orchid",
  "peru",
  "pink",
  "plum",
  "purple",
  "red",
  "salmon",
  "sienna",
  "silver",
  "snow",
  "tan",
  "teal",
  "thistle",
  "tomato",
  "turquoise",
  "violet",
  "white",
  "yellow",
];

var speechRecognitionList = new SpeechGrammarList();
var grammar = "#JSGF V1.0; grammar colors; public <color> = " + colors.join(" | ") + " ;";
speechRecognitionList.addFromString(grammar, 1);
recognition.grammars = speechRecognitionList;
recognition.continuous = true;
recognition.lang = "en-US";
recognition.interimResults = true;
recognition.maxAlternatives = 1;

startBtn.addEventListener("click", () => {
  recognition.start();
  console.log("LISTENING");
});

stopBtn.addEventListener("click", () => {
  console.log("CONTINUOUS LISTENING STOPPED");
  recognition.stop();
});
recognition.onresult = (event) => {
  console.log(event.results);
  var noOfPhrases = event.results.length;
  // console.log(noOfPhrases);
  var lastSentence = event.results[noOfPhrases - 1][0].transcript;
  result.innerHTML = result.innerHTML + " " + lastSentence;
};

recognition.onspeechend = () => {
  console.log("STOPPED LISTENING");
  recognition.stop();
};
