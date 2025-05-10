let heroImg = ["https://images.unsplash.com/photo-1580281780460-82d277b0e3f8?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1yZWxhdGVkfDN8fHxlbnwwfHx8fHw%3D", "https://plus.unsplash.com/premium_photo-1682130157004-057c137d96d5?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8aG9zcGl0YWx8ZW58MHx8MHx8fDA%3D", "https://plus.unsplash.com/premium_photo-1682130157004-057c137d96d5?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8aG9zcGl0YWx8ZW58MHx8MHx8fDA%3D", "https://images.unsplash.com/photo-1512678080530-7760d81faba6?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8aG9zcGl0YWx8ZW58MHx8MHx8fDA%3D", "https://plus.unsplash.com/premium_photo-1664475477169-46b784084d4e?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OXx8aG9zcGl0YWx8ZW58MHx8MHx8fDA%3D"]
let i=(-1);

document.querySelector("#rt").onclick = function() {
    i++;
    data=document.querySelector(".hero");
    data.style.background = `url("${heroImg[i]}")`;
    
}

document.querySelector("#lt").onclick = function() {
    i--;
    data=document.querySelector(".hero");
    data.style.background = `url("${heroImg[i]}")`;
    
}