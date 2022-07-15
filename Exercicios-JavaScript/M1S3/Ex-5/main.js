const output = document.getElementById('output');

const horarioAgora = () => {
  const horario = new Date();
  output.innerHTML = horario.toLocaleTimeString(
    navigator.language,
    {
      hour: '2-digit',
      minute:'2-digit',
      second: '2-digit'
    }
  );
};

setInterval(horarioAgora, 1000);