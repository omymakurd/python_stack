function showTime(){
    const now = new Date();
    document.getElementById("time").innerText=now.toLocaleString();
}
setInterval(showTime,1000)