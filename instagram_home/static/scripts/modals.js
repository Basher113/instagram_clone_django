// Login Modal SHOW START
$('.js-switch-button').click(() => {
    $('.js-login-modal-container').show()

    $('html, body').css({
        overflow: 'hidden',
        height: '100%',
    });

    $('.js-login-modal-close-button').click(() => {
        $('.js-login-modal-container').hide()

        $('html, body').css({
            overflow: 'auto',
            height: 'auto'
        });
    })
})
// LOGIN MODAL SHOW END

// CREATE POST MODAL START
$('.js-create-sidebar-link').click(() => {
    $('.js-create-modal-container').show();

    $('.js-create-modal-close-button').click(() => {
        $('.js-create-modal-container').hide();
    })
})

// CREATE POST MODAL END