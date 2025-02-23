const API_URL = "http://myurl.com"
const MESSAGE_ERRORS = {
    "apiError": "Opss, parece que estamos fora do ar, espere mais alguns minutos...",
    "invalidCredentials": "Usuário ou senha incorreto!",
    "inputError": "Verifique os campos novamente!",
    "usernameError": "Nome de usuário inválido. Deve começar com uma letra e ter de 3 a 16 caracteres.",
    "emailError": "Email inválido. Use um formato como exemplo@gmail.com.",
    "passwordError": "Senha inválida. Deve ter pelo menos 8 caracteres, incluindo 1 letra maiúscula, 1 letra minúscula, 1 número e 1 caractere especial (como !, @, #, $, etc.).",
    "confirmPasswordError": "As senhas não coincidem. Por favor, verifique os campos de senha e confirmação."
}

function handle_error(messageType, value="") {
    let error_message = MESSAGE_ERRORS[messageType]
    
    let response = error_message.indexOf("{VALUE}") ?
    error_message.replace("{VALUE}", value) : value
    
    document.getElementById('error-message').innerText = response
    return false
}

function handle_inputs(inputs) {
    const submitButton = document.getElementById('submit-btn');
    let inputValues = []
    inputs.forEach((x) => {
        if (x.value != '') {
            inputValues.push(x.value)
        }
    });
    
    if (inputValues.length !== inputs.length) {
        // Verifica se algum input é vazio
        handle_error("inputError")
    } else if (submitButton.isActive) {
        return
    } else {
        antiSpam()
        return true
    }
}

function antiSpam() {
    let submitButton = document.getElementById('submit-btn');
    // Anti-spam
    submitButton.isActive = true;
    setTimeout(() => {
        submitButton.isActive = false
    }, 2000);
}

function login() {
    document.getElementById('error-message').innerText = ""
    const inputs = [
        document.getElementById('username-input'),
        document.getElementById('password-input')
    ];

    if (!handle_inputs(inputs)) {
        return
    }

    document.getElementById('error-message').innerText = ""
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
        handle_error("apiError");
    })
} 


function createAccount() {
    const inputs = [
        document.getElementById('username-input'),
        document.getElementById('email-input'),
        document.getElementById('password-input'),
        document.getElementById('confirm-password-input')
    ];

    const usernameRequirements = (username) => {
        const nameRegex = /^[a-zA-Z][a-zA-Z0-9]{2,15}$/;
        if (!nameRegex.test(username) ) {
            return handle_error('usernameError')
        }
        return true
    }

    const emailRequirements = (email) => {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
         // Valida o formato de email
        if (!emailRegex.test(email)) {
            return handle_error('emailError');
        }
        return true;
    };
    
    const passwordRequirements = (password, confirmPassword) => {
        const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[.$!%*?&])[A-Za-z\d.$!%*@#?&]{8,}$/;
        // ^ Pelo menos 8 caracteres, ao menos 1 letra e 1 número
        if (!passwordRegex.test(password)) {
            return handle_error('passwordError');
        } else if (password != confirmPassword) {
            return handle_error('confirmPasswordError')
        }
        return true;
    };

    if (!handle_inputs(inputs)) {
        return
    }

    if (!usernameRequirements(inputs[0].value)) {
        return
    } else if (!emailRequirements(inputs[1].value)) {
        return
    } else if (!passwordRequirements(inputs[2].value, inputs[3].value)) {
        return
    }

    document.getElementById('error-message').innerText = ""
    const request = fetch(`${API_URL}/account/register`, {
        method: "POST",
        headers: { "Content-type": "application/json" },
        body: JSON.stringify(
            {
            username: inputs[0].value,
            email: inputs[1].value,
            password: inputs[2].value
            }
        )
    }).then(async(res) => {
        // Aqui deve ser validada a resposta da api futuramente...
        response_json = await res.json();
    }, (error) => {
        handle_error("apiError");
    })
}