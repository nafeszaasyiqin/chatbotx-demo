
			const user_id = "u1"; //simple session tracking
			const chatbox = document.getElementById("chatbox");

			const defaultOptions = ["Hi", "Hello", "Thank you", "Ask outlet", "Operating hours"];

			//Do quick chat
			function showOptions(options){
				const optionsDiv = document.getElementById("options");
				optionsDiv.innerHTML = "";
				options.forEach(opt =>{
					const button = document.createElement("button");
					button.textContent = opt;
					button.onclick = () => {
						sendMessage(opt); //send the clicked bubble

					};
					optionsDiv.appendChild(button);
				});
			}

			// Show default options initially
			showOptions(defaultOptions);
			
			
			async function sendMessage(predefinedMessage){
				const input = document.getElementById("input");
				const message = predefinedMessage || input.value;
				if(!message)return;

				//Show user message
				chatbox.innerHTML +=`<div class="user"><b>You:</b> ${message}</div>`;
				input.value="";

				//Clear the bubbles
				document.getElementById("options").innerHTML="";

				//Send message to backend
				const response = await fetch("https://chatbotx-demo.onrender.com/chat", {
					method:"POST",
					headers: {"Content-Type": "application/json"},
					body: JSON.stringify({user_id,mesej:message}),
				});

				const data = await response.json();
				chatbox.innerHTML += `<div class="bot"><b>Botx:</b> ${data.response}
				</div>`;
				chatbox.scrollTop = chatbox.scrollHeight;

				showOptions(defaultOptions);

				//eg:show bubble for next turn
				if (data.response.includes("Which outlet")){
					showOptions(["SS2","Cyberjaya", "Cheras", "Ampang", "Bangi"]);
				}

				




			}
			