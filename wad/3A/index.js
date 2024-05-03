//first create a public folder and create a html file in it

const express = require('express');

const app = express();

app.use(express.static('public'));
app.listen(4000, () => {
    console.log('server is started');
})