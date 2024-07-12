const sudoku = [
    ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.']
];

document.addEventListener('DOMContentLoaded', () => {
    const rows = document.querySelectorAll('tr');

    for (let i = 0; i < rows.length; i++) {
        const elements = rows[i].querySelectorAll('td');
        for (let j = 0; j < elements.length; j++) {
            let td = elements[j];
            let input = td.querySelector('input');
            input.id = `${i},${j}`;
            input.addEventListener('change', event => {
                updateSudoku(event.target);
            })
        }
    }
})

function updateSudoku(text) {
    let id = text.id.split(',');
    let y = id[0];
    let x = id[1];
    sudoku[y][x] = text.value;
    document.querySelector('#hidden').value = JSON.stringify(sudoku);
}