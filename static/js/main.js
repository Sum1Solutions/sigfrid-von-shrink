// Retrieve elements from the DOM for the chat messages, user input field, and the send button
const chatMessages = document.getElementById('chat-messages');
const userInput = document.getElementById('user-input');
const sendButton = document.getElementById('send-button');

/**
 * This function is used to add a message to the chat window.
 * @param {string} message - The content of the message to be added.
 * @param {string} sender - The sender of the message, e.g., 'User' or 'AI Therapist'.
 */
const addMessage = (message, sender) => {
    // Create a new 'div' element to contain the message
    const messageElement = document.createElement('div');
    // Add a 'message' CSS class to the new div
    messageElement.classList.add('message');

    // Depending on who the sender is, add the appropriate CSS class
    if (sender === 'User') {
        messageElement.classList.add('user-message');
    } else {
        messageElement.classList.add('therapist-message');
    }

    // Populate the messageElement with formatted HTML content
    messageElement.innerHTML = `<p><strong>${sender}:</strong> ${message}</p>`;

    // Append the new message to the chat window
    chatMessages.appendChild(messageElement);

    // Scroll the chat window to the bottom so the new message is visible
    chatMessages.scrollTop = chatMessages.scrollHeight;
};

/**
 * This function handles the user's input when they send a message.
 */
const handleUserInput = async () => {
    // Trim white spaces from the user input and store it in a variable
    const userMessage = userInput.value.trim();

    // If the user input is empty, return early to prevent sending an empty message
    if (userMessage.length === 0) {
        return;
    }

    // Add the user's message to the chat window
    addMessage(userMessage, 'User');

    // Clear the user input field
    userInput.value = '';

    // Use a try-catch block to handle potential errors when communicating with the AI therapist
    try {
        // Send a POST request to the '/chat' endpoint with the user's message
        const response = await axios.post('/chat', { message: userMessage });
        // Extract the AI therapist's message from the response
        const therapistMessage = response.data.message;
        // Add the AI therapist's message to the chat window
        addMessage(therapistMessage, 'AI Therapist');
    } catch (error) {
        // Log any errors that occurred
        console.error('Error communicating with AI therapist:', error);
    }
};

// Add an event listener to the send button to handle click events
sendButton.addEventListener('click', handleUserInput);

// Add an event listener to the user input field to handle the 'Enter' key press
userInput.addEventListener('keydown', (event) => {
    // If the pressed key is 'Enter', handle the user input
    if (event.key === 'Enter') {
        handleUserInput();
    }
});
