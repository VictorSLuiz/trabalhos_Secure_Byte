function verificarLogin() {

    const usuarioDigitado = document.getElementById("usuario").value;
    const senhaDigitada = document.getElementById("senha").value;

    let encontrado = false;

    const usuariosPermitidos = [
        { usuario: "victor", senha: "123" },
        { usuario: "bruno", senha: "senha123" },
        { usuario: "joao", senha: "456" }
    ];

    const mensagem = document.getElementById("mensagem");

   // const loginValido = usuariosPermitidos.some(u => u.usuario === usuarioDigitado && u.senha === senhaDigitada);
    for (let i = 0; i < usuariosPermitidos.length; i++) {
        if ( usuarioDigitado === usuariosPermitidos[i].usuario  && senhaDigitada === usuariosPermitidos[i].senha) {
           encontrado=true;
           
            mensagem.innerHTML = "Login feito com sucesso!";
            return;
        }
    }
    if (!encontrado) {
        mensagem.innerHTML = "Usuário ou senha incorretos. Tente novamente.";
    } 

    }