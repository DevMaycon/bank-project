const API_URL = "http://myurl.com"
const MESSAGE_ERRORS = {
    "inputError": "Verifique os campos novamente!",
    "invalidCredential": "Usuario ou senha incorreto!",
    "loginError": "Opss, parece que estamos fora do ar, espere mais alguns minutos...",
    "tooManyRequests": "Espere um tempo antes de enviar novamente!"
}

function handle_error(messageType, value="") {
    let error_message = MESSAGE_ERRORS[messageType]
    
    let response = error_message.indexOf("{VALUE}") ?
    error_message.replace("{VALUE}", value) : value
    
    document.getElementById('error-message').innerText = response
}

async function login() {
    const inputs = [
        document.getElementById('username-input'),
        document.getElementById('password-input')
    ];
    const submitButton = document.getElementById('submit-btn');

    if (inputs[0].value == "" || inputs[1].value == "") {
        return handle_error("inputError")
    } else if (submitButton.isActive) {
        return handle_error("tooManyRequests")
    }

    submitButton.isActive = true;
    setTimeout(() => {
        submitButton.isActive = false
        }, 5000
    )

    const request = fetch(`${API_URL}/auth`, {
        method: "POST",
        headers: { "Content-type": "application/json" },
        body: JSON.stringify({
            username: inputs[0].value,
            password: inputs[1].value
        })
    }).then(async(res) => {
        // Aqui deve ser validada a resposta da api futuramente...
        response_json = await res.json();

    }, (error) => {
        handle_error("loginError");
    })
}