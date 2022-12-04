console.log('Hi')
console.log(window.location.href)

//$.ajax({
//type: 'GET',
//url: `${window.location.href}data`,
//success: function(response) {
//    console.log(response)
//}
//})

const getData = () => {
   // const data = document.currentScript.dataset
    const questions = data.questions
    return questions
}

window.addEventListener('load', () => {
    let res = getData()
    console.log(res)
})