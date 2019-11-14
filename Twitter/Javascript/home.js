// document.getElementById("tweets-1").addEventListener('l')
window.addEventListener('load', tweetDisplay)

let tweetHttpRequest;

function tweetDisplay() {
    tweetHttpRequest = new XMLHttpRequest();
    if (!tweetHttpRequest) {
        alert("Could not create request!");
        return false;
    }

    tweetHttpRequest.onreadystatechange = tweetResponse;
    tweetHttpRequest.open('GET', 'http://127.0.0.1:8000/tweet');
    tweetHttpRequest.send();
}

function tweetResponse() {
    if (tweetHttpRequest.readyState === XMLHttpRequest.DONE) {
        if (tweetHttpRequest.status === 200) {
            // console.log(tweetHttpRequest.responseText);
            let tweetData = JSON.parse(tweetHttpRequest.responseText);
            let idtweetData = document.getElementById('tweet-1');
            for (let i = 0; i < tweetData.length; i++) {
                let obj = tweetData[i];
                idtweetData.insertAdjacentHTML('beforeend', '<div id="tweet-structure">' + obj.tweet_box + '<br>' + obj.user + '<br>' + obj.date_updated + '</div>')
                console.log(tweetData)
            }
        }
    }
}