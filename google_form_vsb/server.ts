import express, { Request, Response } from 'express';
import bodyParser from 'body-parser';
import fs from 'fs';
import path from 'path';

const app = express();
const port = 3000;

// Middleware to parse JSON bodies
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// POST endpoint to receive form data
app.post('/submit-form', (req: Request, res: Response) => {
    const formData = req.body;
    console.log('Received form data:', formData);

    // Define the path to the JSON file
    const jsonFilePath = path.join(__dirname, 'form-data.json');

    // Write the form data to the JSON file
    fs.writeFile(jsonFilePath, JSON.stringify(formData, null, 2), (err) => {
        if (err) {
            console.error('Error saving form data:', err);
            res.status(500).send('Error saving form data');
        } else {
            console.log('Form data saved successfully');
            res.send('Form submitted and data saved as JSON');
        }
    });
});

// Start the server
app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
