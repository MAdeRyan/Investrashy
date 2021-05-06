// var socket = io()
//         $(function () {
//             $("#kirim").click(function () {
//                 var pesan = {nama: $("#nama").val(), pesan: $("#pesanKirim").val()}
//                 postPesan(pesan)
//             })
//             getPesan()
//         });

//         socket.on('pesan', tambahPesan)
//         function tambahPesan(pesan) {
//             $("#pesan").append(`<div class="send-messages">
//                                     <p class="message-detail"> Kepada: ${pesan.nama} </p>
//                                     <p class="messages-content">${pesan.pesan}</p>
//                                     <div class="message-timestamp-right">SMS 13:37</div>
//                                 </div>`)
//         }

//         function getPesan() {
//             $.get('http://localhost:3000/pesan', function (data) {
//                 data.forEach(tambahPesan)
//             })
//         }

//         function postPesan(pesan) {
//             $.post('http://localhost:3000/pesan', pesan)
//         }