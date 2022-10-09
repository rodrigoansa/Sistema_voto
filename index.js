import express from 'express';
import cors from 'cors';

const governadores = [
    {
        "name": 'Xuxa',
        "number": '10',
        "votes": 0,
    },
    {
        "name": 'Eliana',
        "number": '15',
        "votes": 0,
    },
    {
        "name": 'Angélica',
        "number": '22',
        "votes": 0,
    },
    {
        "name": 'Jaqueline',
        "number": '32',
        "votes": 0,
    }
]

const app = express();
app.use(cors());
app.use(express.json());

app.get('/', (req, res) => {
    return res.status(200).json({
        status: 'online',
        erros: 0
    });
});

app.get('/candidatos/governadores', (req, res) => {
    return res.status(200).json({
        governadores,
    });
});

app.listen(3333, () => {
    console.log('Server iniciado na porta 3333');
});