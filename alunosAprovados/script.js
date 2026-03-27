async function carregarAlunos() {
  const resposta = await fetch('alunos.json');
  const alunos = await resposta.json();

  mostrarAlunosAprovados(alunos);
}

function mostrarAlunosAprovados(listaAlunos) {
  const div = document.getElementById('resultado');

  for (let i = 0; i < listaAlunos.length; i++) {
    const aluno = listaAlunos[i];

    let soma = 0;
    for (let j = 0; j < aluno.notas.length; j++) {
      soma += aluno.notas[j];
    }

    const media = soma / aluno.notas.length;

    if (media >= 7) {
      const p = document.createElement('p');
      p.innerHTML = `
        Nome: ${aluno.nome} <br>
        Média: ${media.toFixed(2)} <br>
        Curso: ${aluno.curso}
        <hr>
      `;

      div.appendChild(p);
    }
  }
}

carregarAlunos();