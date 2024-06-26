import { csrftoken } from "./utils.js";


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
        unrenderUploadImage()
    })
})

// CREATE POST MODAL END


const imageInput = document.querySelector('#create-image-input')


const createPost = async () => {
    const image = imageInput.files[0];
    const caption = $('#caption-content').val()
    let formData = new FormData();

    formData.append('content', image);
    formData.append('caption', caption)
    const newPost = await fetch('http://127.0.0.1:8000/api/create-post/', {
        method: 'POST',
        body: formData,
        headers: {
            'X-CSRFTOKEN': csrftoken
        }
    }).then((response) => {
        return response.json()
    }).catch(error => { console.error(error) })
    unrenderUploadImage()
    $('.js-create-modal-container').hide()
}


function renderUploadImage() {
    let imgLink = URL.createObjectURL(imageInput.files[0])
    $('.js-middle-content-container').hide()
    $('#create-uploaded-image').show()
    $('.js-share-button').show()
    $('.js-create-modal-content').addClass('create-modal-content-wider')
    $('.js-post-caption-container').show()
    $('#create-uploaded-image').attr('src', imgLink)
}

function unrenderUploadImage() {
    $('.js-middle-content-container').show()
    $('#create-uploaded-image').hide()
    $('.js-share-button').hide()
    $('.js-post-caption-container').hide()
    $('.js-create-modal-content').removeClass('create-modal-content-wider')
}


imageInput.addEventListener('change', (event) => {
    event.preventDefault();
    console.log('success?')
    renderUploadImage()
})

$('.js-share-button').click(() => {
    createPost();
})


// Post detail X button
