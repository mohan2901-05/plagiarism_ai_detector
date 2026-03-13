async function analyze(){

let text = document.getElementById("inputText").value;

let fileInput = document.getElementById("fileUpload");

let formData = new FormData();

if(fileInput.files.length > 0){

formData.append("file", fileInput.files[0]);

}

else{

formData.append("text", text);

}

let response = await fetch("http://127.0.0.1:5000/analyze",{

method:"POST",

body:formData

});

let data = await response.json();

document.getElementById("result").innerHTML = `

Plagiarism Score: ${data.plagiarism_score}% <br>
Matched Source: ${data.matched_source} <br>
AI Generated Probability: ${data.ai_probability}%

`;

}