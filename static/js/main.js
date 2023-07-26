const chatMessages = document.getElementById('chat-messages');
const userInput = document.getElementById('user-input');
const sendButton = document.getElementById('send-button');

const addMessage = (message, sender) => {
    const messageElement = document.createElement('div');
    messageElement.classList.add('message');

    if (sender === 'User') {
        messageElement.classList.add('user-message');
    } else {
        messageElement.classList.add('therapist-message');
    }

    messageElement.innerHTML = `<p><strong>${sender}:</strong> ${message}</p>`;
    chatMessages.appendChild(messageElement);

    chatMessages.scrollTop = chatMessages.scrollHeight;
};

const handleUserInput = async () => {
    const userMessage = userInput.value.trim();

    if (userMessage.length === 0) {
        return;
    }

    addMessage(userMessage, 'User');

    userInput.value = '';

    try {
        const response = await axios.post('/chat', { message: userMessage });
        const therapistMessage = response.data.message;
        addMessage(therapistMessage, 'AI Therapist');
    } catch (error) {
        console.error('Error communicating with AI therapist:', error);
    }
};

sendButton.addEventListener('click', handleUserInput);

userInput.addEventListener('keydown', (event) => {
    if (event.key === 'Enter') {
        handleUserInput();
    }
});
