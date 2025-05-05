document.getElementById("contratanteForm").addEventListener("submit", async function (e) {
    e.preventDefault();

    const contratante = {
        CPF: parseInt(document.getElementById("CPF").value),
        nome: document.getElementById("nome").value,
        telefone: document.getElementById("telefone").value,
        telefone_emergencia: document.getElementById("telefone_emergencia").value,
        email: document.getElementById("email").value,
        senha: document.getElementById("senha").value,
        endereco: document.getElementById("endereco").value,
        genero: document.getElementById("genero").value,
        data_nascimento: document.getElementById("data_nascimento").value
    };

    try {
        const response = await fetch("http://127.0.0.1:8000/api/contratante/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(contratante)
        });

        if (!response.ok) {
            const errorData = await response.json();
            throw new Error("Erro ao cadastrar: " + JSON.stringify(errorData));
        }

        alert("Contratante cadastrado com sucesso!");
        listarContratantes();
    } catch (error) {
        alert(error.message);
    }
});

async function listarContratantes() {
    const lista = document.getElementById("contratanteList");
    lista.innerHTML = "";

    try {
        const response = await fetch("http://127.0.0.1:8000/api/contratante/");
        const data = await response.json();

        data.forEach(c => {
            const item = document.createElement("li");
            item.textContent = `${c.nome} - ${c.email}`;
            lista.appendChild(item);
        });
    } catch (error) {
        console.error("Erro ao carregar contratantes:", error);
    }
}

// Carregar lista ao iniciar
listarContratantes();
