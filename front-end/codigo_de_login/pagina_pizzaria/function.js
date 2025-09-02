
        async function carregarPizza(pizza) {
        try{
            document.getElementById("detalhes").innerHTML = "Carregando informações..."
            await new Promise(resolve => setTimeout(resolve , 2000));
            let mensagens = {
                "Calabresa" : "A especiaria da casa, e a melhor da região",
                "Moda": "A pizza que vai fazer delirar de gostosura",
                "4queijos": "Feita com os melhores queijos do mercado",
                "Portuguesa": "Passada de geração e geração"
            };
            document.getElementById("detalhes").innerHTML = mensagens[pizza];
        }
        catch (erro) {
            document.getElementById("detalhes").innerHTML = "Erro :" + erro.mensagens
        }}

        function voltar() {
            window.location.href = "../index.html";
        }