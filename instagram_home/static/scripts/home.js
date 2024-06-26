// document.querySelector('.js-switch-button').addEventListener('click', () => {
//     document.querySelector('.modal-container').style.display = 'inline'
//     console.log('I am clicked')

//     document.querySelector('.js-close-button').addEventListener('click', () => {
//         document.querySelector('.modal-container').style.display = 'none'
//     })
// })
import { csrftoken } from "./utils.js";
function renderPostDetail(postId) {
    $.ajax({
        type: 'GET',
        url: `http://127.0.0.1:8000/api/post-detail/${postId}`,
        success: (response) => {
            let html = `
                <div class="post-detail-image-container">
                    <img src=${response.content} alt="IVE 1st World Tour Poster">
                </div>
                <div class="post-detail-right-section">
                    <div class="post-detail-post-content">
                        <div><img src=${response.author.profile.image} alt="" id="post-detail-author-profile"> <strong>${response.author.username}</strong></div>
                        
                    </div>
                    <div class="comments">
                        ${renderComments(response.comments)}
                    </div>
                    <div class="post-detail-icons-container">
                        <div class="heart-comment-share">
                            <i class="bi bi-heart post-detail-heart-icon"></i>
                            <i class="bi bi-chat  post-detail-chat-icon"></i>
                            <i class="bi bi-send  post-detail-send-icon"></i>
                        </div>
                        <div class="post-detail-shared-icon-container">
                            <i class="bi bi-bookmark post-detail-save-icon"></i>
                        </div>
                    </div>
                    
                    <div class="likes">46,622 likes</div>

                    <div class="post-detail-comment-input-container">
                        <i class="bi bi-emoji-smile post-detail-emoji-icon"></i>
                        <input type="text" placeholder="Add a comment" id="comment-input-${response.id}">
                        <button type="submit" id="post-modal-comment-${response.id}">Post</button>
                    </div>
                </div>
            `;
            document.querySelector('.js-post-modal-content').innerHTML = html;
            $(`#post-modal-comment-${response.id}`).click(() => {
                addComment(response.id)
            })
            $(`#comment-input-${response.id}`).keypress((event) => {
                if (event.key === 'Enter') {
                    addComment(response.id)
                }
            })
            $('.js-post-detail-modal').show()
        }
    })
}

// Render Comments of Post
function renderComments(comments) {
    // loop over comments
    let html = '';
    comments.forEach(async (comment) => {
        html +=
            `
            <div class="comment">
                <img src="${comment.author.profile.image}" alt="User profile picture">
                <p><strong>${comment.author.username}</strong> ${comment.content}</p>
            </div>
            `
    })
    return html;
}

document.querySelectorAll('.view-all-comment').forEach((postDetail) => {
    postDetail.addEventListener('click', () => {
        const postId = postDetail.dataset.postId;
        renderPostDetail(postId);
    })
})

$('.post-detail-close-button').click(() => {
    $('.js-post-detail-modal').hide()
})


// Add comments in Post Detail
function addComment(postId) {
    const commentInput = document.querySelector(`#comment-input-${postId}`)
    const commentContent = commentInput.value
    $.ajax({
        type: 'POST',
        url: 'http://127.0.0.1:8000/api/create-comment/',
        data: {
            post: postId,
            content: commentContent,
            csrfmiddlewaretoken: csrftoken
        },
        success: (response) => {
            commentInput.value = '';
            renderPostDetail(postId);
        }
    })
}

