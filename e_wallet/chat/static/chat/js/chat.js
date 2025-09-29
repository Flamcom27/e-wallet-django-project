// console.log(djangoContext.user)
// console.log(djangoContext.reciever)
const url = `ws://${window.location.host}/chat/ws/send-message/`;
const chatSocket = new WebSocket(url);
const form = document.querySelector("#message-form>form")
const textArea = form.querySelector('textarea')
const messageWindow = document.querySelector("#messages>div")

function sendMessage(message) {
    chatSocket.send(JSON.stringify({message: message}));
}

function appendMessage(message, sender){
    const container = document.createElement("div");
    const image = `
        <a href="/profile/${sender.pk}/">
            <img src="${sender.img}" alt="profile_image" class="profile-image message-image">
        </a>
    `;
    container.classList.add(sender.side);
    container.innerHTML = `
        <div class="message">
            <p>${message}</p>
        </div>
    `;
    if (sender.side === "left") {
        container.innerHTML = image + container.innerHTML;
    } else {
        container.innerHTML += image;
    }
    messageWindow.appendChild(container);
    scrollToBottom();
}

chatSocket.addEventListener("message", e => {
    
    const data = JSON.parse(e.data);
    appendMessage(data.message, djangoContext.reciever);
})
form.addEventListener("submit", e => {
    e.preventDefault();
    sendMessage(textArea.value);
    appendMessage(textArea.value.replaceAll('\n', '<br>'), djangoContext.user);
    textArea.value = "";
})
function scrollToBottom() {
    let relative = document
        .getElementById("messages")
        .getElementsByTagName("div")[0];
    relative.scrollTop = relative.scrollHeight;
}
scrollToBottom()
