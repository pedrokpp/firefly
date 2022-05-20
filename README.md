# Firefly
Jogo desenvolvido para a aula de Programação de Jogos, Universidade Federal Fluminense

Utilizamos [PPlay](https://github.com/adonisgasiglia/pplay), uma "framework" baseada no [pygame](https://www.pygame.org/news)

*O PPlay por ser muito antigo, foi brevemente modificado em certos métodos para facilitar o uso entre pygame e PPlay*

## Alunos
Dawson e Pedro

## Métodos do PPlay atualizados
As mudanças mais relevantes serão documentadas aqui, caso queira ver exatamente quais features foram adicionadas e tiradas, basta olhar nos commits

 - `Window.draw_text`
    - Para facilitar a portabilidade do jogo, foi adicionado um argumento adicional `file_path: bool` para indicar se `font_name` é um path e não um nome
