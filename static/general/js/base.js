function exibir_form(tipo){

    cardapio_desire = document.getElementById('cardapio_teste')
    cardapio_c1 = document.getElementById('c1')
    cardapio_c2 = document.getElementById('c2')
    cardapio_c3 = document.getElementById('c3')
    cardapio_c4 = document.getElementById('c4')

    if (tipo == 1){

        cardapio_desire.style.display = 'block'
        cardapio_c1.style.display = 'none'
        cardapio_c2.style.display = 'none'
        cardapio_c3.style.display = 'none'
        cardapio_c4.style.display = 'none'


    }else if(tipo == 2){

        cardapio_desire.style.display = 'none'
        cardapio_c1.style.display = 'block'
        cardapio_c2.style.display = 'block'
        cardapio_c3.style.display = 'block'
        cardapio_c4.style.display = 'block'

    }


}