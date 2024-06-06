// document.querySelector('.js-switch-button').addEventListener('click', () => {
//     document.querySelector('.modal-container').style.display = 'inline'
//     console.log('I am clicked')
    
//     document.querySelector('.js-close-button').addEventListener('click', () => {
//         document.querySelector('.modal-container').style.display = 'none'
//     })
// })

$('.js-switch-button').click(() => {
    $('.modal-container').show()

    $('html, body').css({
        overflow: 'hidden',
        height: '100%',
    });

    $('.js-close-button').click(() => {
        $('.modal-container').hide()

        $('html, body').css({
            overflow: 'auto',
            height: 'auto'
        });
    })

    

})



