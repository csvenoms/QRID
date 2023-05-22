// chat.js
const room_id = document.currentScript.getAttribute('data-room-id');
const chatSocket = new WebSocket(
    'ws://' + window.location.host +
    '/ws/chat/' + room_id + '/');

chatSocket.onmessage = function(event) {
    const message = JSON.parse(event.data);
    const messageList = document.querySelector('#messages');
    const messageItem = document.createElement('li');
    messageItem.innerHTML = '<b>' + message.username + ':</b> ' + message.content;
    messageList.appendChild(messageItem);
};

document.querySelector('#message-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const messageInput = document.querySelector('#message-input');
    const messageContent = messageInput.value;
    const messageData = {
        'room_id': room_id,
        'content': messageContent
    };
    chatSocket.send(JSON.stringify(messageData));
    messageInput.value = '';
});