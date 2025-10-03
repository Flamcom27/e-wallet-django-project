const url = `ws://${window.location.host}/chat/ws/send-message/`;
const chatSocket = new WebSocket(url);
const form = document.querySelector("#message-form>form");
const textArea = form.querySelector('textarea');
const messageWindow = document.querySelector("#messages>div");

// [ ]TODO restart WebSocket Connection when user opens a tab
function scrollToBottom() {
    let relative = document
        .getElementById("messages")
        .getElementsByTagName("div")[0];
    relative.scrollTop = relative.scrollHeight;
}

function sendMessage(type, content) {
    chatSocket.send(JSON.stringify({
        type: type,
        ...content
    }));
}

function appendMessage(message, sender){
    message = message.replaceAll('\n', '<br>');
    const container = document.createElement("div");
    console.log(sender);
    const image = `
        <a href="/profile/${sender.pk}/">
            <img src="${sender.iconUrl}" alt="profile_image" class="profile-image message-image">
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
    if (data.type === 'message'){
        const reciever = djangoContext.reciever;
        const user = djangoContext.user;
        const sender = data.sender == reciever.pk ? reciever : user
        appendMessage(data.message, sender);
    } else if (data.type === 'context'){
        sendMessage("context", {chatId: djangoContext.chatId});
    }
})

form.addEventListener("submit", e => {
    e.preventDefault();
    if (textArea.value.trim().length !== 0){
        sendMessage("message", {
            "message": textArea.value,
            "sender": djangoContext.user.pk
        });
        // appendMessage(textArea.value, djangoContext.user);
        textArea.value = "";
    }
})

scrollToBottom();
