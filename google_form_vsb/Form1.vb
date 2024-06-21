Imports System.Net.Http
Imports System.Text
Imports Newtonsoft.Json
Imports MongoDB.Driver
Imports MongoDB.Bson

Public Class Form1
    ' Declare form controls and MongoDB client
    Private WithEvents btnSubmit As Button
    Private WithEvents btnCancel As Button
    Private lblTitle As Label
    Private lblDetails As Label
    Private lblName As Label
    Private txtName As TextBox
    Private lblGender As Label
    Private cmbGender As ComboBox  ' Changed from checkboxes to dropdown
    Private lblEmail As Label
    Private txtEmail As TextBox
    Private lblDateOfBirth As Label
    Private dtpDateOfBirth As DateTimePicker
    Private lblFavoriteColor As Label
    Private txtFavoriteColor As TextBox
    Private lblFavoriteAnime As Label
    Private txtFavoriteAnime As TextBox
    Private lblGojoReturn As Label
    Private rbGojoYes As RadioButton
    Private rbGojoNo As RadioButton
    Private lblColorOfSky As Label
    Private cmbColorOfSky As ComboBox
    Private mongoClient As MongoClient
    Private formsCollection As IMongoCollection(Of BsonDocument)

    ' Form Load event
    Private Sub Form1_Load(sender As Object, e As EventArgs) Handles MyBase.Load
        ' Initialize the form controls
        InitializeControls()
        ' Initialize MongoDB connection
        InitializeMongoDB()
    End Sub

    ' Method to initialize form controls
    Private Sub InitializeControls()
        Me.BackColor = Color.LightBlue

        ' Initialize the labels
        lblTitle = New Label()
        lblTitle.Text = "Google like forms"
        lblTitle.Font = New Font("Times New Roman", 12, FontStyle.Bold)
        lblTitle.Location = New Point(300, 20)
        lblTitle.AutoSize = True
        Me.Controls.Add(lblTitle)

        lblDetails = New Label()
        lblDetails.Text = "🔫 Hurry! Put your Details in the box"
        lblDetails.Font = New Font("Tahoma", 10, FontStyle.Italic)
        lblDetails.Location = New Point(50, 60)
        lblDetails.AutoSize = True
        Me.Controls.Add(lblDetails)

        lblName = New Label()
        lblName.Text = "Name:"
        lblName.Location = New Point(50, 90)
        lblName.AutoSize = True
        Me.Controls.Add(lblName)

        txtName = New TextBox()
        txtName.Location = New Point(250, 90)
        txtName.Size = New Size(150, 20)
        Me.Controls.Add(txtName)

        lblGender = New Label()
        lblGender.Text = "Gender:"
        lblGender.Location = New Point(50, 120)
        lblGender.AutoSize = True
        Me.Controls.Add(lblGender)

        cmbGender = New ComboBox()
        cmbGender.DropDownStyle = ComboBoxStyle.DropDownList
        cmbGender.Items.AddRange(New String() {"Male", "Female", "Other"})
        cmbGender.Location = New Point(250, 120)
        cmbGender.Size = New Size(150, 20)
        Me.Controls.Add(cmbGender)

        lblEmail = New Label()
        lblEmail.Text = "Email:"
        lblEmail.Location = New Point(50, 150)
        lblEmail.AutoSize = True
        Me.Controls.Add(lblEmail)

        txtEmail = New TextBox()
        txtEmail.Location = New Point(250, 150)
        txtEmail.Size = New Size(150, 20)
        Me.Controls.Add(txtEmail)

        lblDateOfBirth = New Label()
        lblDateOfBirth.Text = "Date of Birth:"
        lblDateOfBirth.Location = New Point(50, 180)
        lblDateOfBirth.AutoSize = True
        Me.Controls.Add(lblDateOfBirth)

        dtpDateOfBirth = New DateTimePicker()
        dtpDateOfBirth.Format = DateTimePickerFormat.Short
        dtpDateOfBirth.Location = New Point(250, 180)
        dtpDateOfBirth.Size = New Size(150, 20)
        Me.Controls.Add(dtpDateOfBirth)

        lblFavoriteColor = New Label()
        lblFavoriteColor.Text = "Favourite color:"
        lblFavoriteColor.Location = New Point(50, 210)
        lblFavoriteColor.AutoSize = True
        Me.Controls.Add(lblFavoriteColor)

        txtFavoriteColor = New TextBox()
        txtFavoriteColor.Location = New Point(250, 210)
        txtFavoriteColor.Size = New Size(150, 20)
        Me.Controls.Add(txtFavoriteColor)

        lblFavoriteAnime = New Label()
        lblFavoriteAnime.Text = "Favorite anime:"
        lblFavoriteAnime.Location = New Point(50, 240)
        lblFavoriteAnime.AutoSize = True
        Me.Controls.Add(lblFavoriteAnime)

        txtFavoriteAnime = New TextBox()
        txtFavoriteAnime.Location = New Point(250, 240)
        txtFavoriteAnime.Size = New Size(150, 20)
        Me.Controls.Add(txtFavoriteAnime)

        lblGojoReturn = New Label()
        lblGojoReturn.Text = "Will Gojo Satoru return?"
        lblGojoReturn.Location = New Point(50, 270)
        lblGojoReturn.AutoSize = True
        Me.Controls.Add(lblGojoReturn)

        rbGojoYes = New RadioButton()
        rbGojoYes.Text = "No"
        rbGojoYes.Location = New Point(250, 270)
        rbGojoYes.AutoSize = True
        Me.Controls.Add(rbGojoYes)

        rbGojoNo = New RadioButton()
        rbGojoNo.Text = "No"
        rbGojoNo.Location = New Point(350, 270)
        rbGojoNo.AutoSize = True
        Me.Controls.Add(rbGojoNo)

        lblColorOfSky = New Label()
        lblColorOfSky.Text = "What is the color of the sky?"
        lblColorOfSky.Location = New Point(50, 300)
        lblColorOfSky.AutoSize = True
        Me.Controls.Add(lblColorOfSky)

        cmbColorOfSky = New ComboBox()
        cmbColorOfSky.DropDownStyle = ComboBoxStyle.DropDownList
        cmbColorOfSky.Items.AddRange(New String() {"Blue", "Black"})
        cmbColorOfSky.Location = New Point(250, 300)
        cmbColorOfSky.Size = New Size(150, 20)
        Me.Controls.Add(cmbColorOfSky)

        ' Initialize the buttons
        btnSubmit = New Button()
        btnSubmit.Text = "Submit"
        btnSubmit.Location = New Point(50, 330)
        btnSubmit.Size = New Size(70, 40)
        Me.Controls.Add(btnSubmit)

        btnCancel = New Button()
        btnCancel.Text = "Cancel"
        btnCancel.Location = New Point(150, 330)
        btnCancel.Size = New Size(70, 40)
        Me.Controls.Add(btnCancel)
    End Sub

    ' Method to initialize MongoDB connection
    Private Sub InitializeMongoDB()
        Try
            ' Set up MongoDB connection
            Dim mongoConnectionString As String = "mongodb://localhost:27017"
            mongoClient = New MongoClient(mongoConnectionString)

            ' Access database and collection
            Dim database As IMongoDatabase = mongoClient.GetDatabase("slidely")
            formsCollection = database.GetCollection(Of BsonDocument)("forms_data")

            MessageBox.Show("MongoDB connection established successfully.")
        Catch ex As Exception
            MessageBox.Show($"Error connecting to MongoDB: {ex.Message}", "MongoDB Connection Error", MessageBoxButtons.OK, MessageBoxIcon.Error)
        End Try
    End Sub

    ' Event handler for Submit button click
    Private Async Sub btnSubmit_Click(sender As Object, e As EventArgs) Handles btnSubmit.Click
        ' Validate input (basic validation for demonstration)
        If String.IsNullOrWhiteSpace(txtName.Text) OrElse
           String.IsNullOrWhiteSpace(txtEmail.Text) OrElse
           String.IsNullOrWhiteSpace(txtFavoriteColor.Text) OrElse
           String.IsNullOrWhiteSpace(txtFavoriteAnime.Text) OrElse
           cmbColorOfSky.SelectedIndex = -1 Then
            MessageBox.Show("Please fill in all fields.", "Validation Error", MessageBoxButtons.OK, MessageBoxIcon.Error)
            Return
        End If

        ' Validate radio button selection
        If Not rbGojoYes.Checked AndAlso Not rbGojoNo.Checked Then
            MessageBox.Show("Please select whether Gojo Satoru will return.", "Validation Error", MessageBoxButtons.OK, MessageBoxIcon.Error)
            Return
        End If

        ' Validate gender selection
        If cmbGender.SelectedIndex = -1 Then
            MessageBox.Show("Please select your gender.", "Validation Error", MessageBoxButtons.OK, MessageBoxIcon.Error)
            Return
        End If

        ' Prepare data to send to server
        Dim data As New Dictionary(Of String, String) From {
            {"name", txtName.Text},
            {"email", txtEmail.Text},
            {"date_of_birth", dtpDateOfBirth.Value.ToString("yyyy-MM-dd")},
            {"favorite_color", txtFavoriteColor.Text},
            {"favorite_anime", txtFavoriteAnime.Text},
            {"gojo_return", If(rbGojoYes.Checked, "Yes", "No")},
            {"gender", cmbGender.SelectedItem.ToString()},
            {"color_of_sky", cmbColorOfSky.SelectedItem.ToString()}
        }

        ' Convert data to JSON string
        Dim jsonContent As String = JsonConvert.SerializeObject(data)
        MessageBox.Show($"JSON Content: {jsonContent}") ' Debug message to verify JSON content
        Dim content As New StringContent(jsonContent, Encoding.UTF8, "application/json")

        ' Send data to backend server (if needed)
        Try
            Dim client As New HttpClient()
            Dim response As HttpResponseMessage = Await client.PostAsync("http://localhost:3000/submit-form", content)

            ' Check response status
            If response.IsSuccessStatusCode Then
                Dim responseString As String = Await response.Content.ReadAsStringAsync()
                MessageBox.Show($"Form submitted successfully! Server response: {responseString}", "Success")
            Else
                MessageBox.Show($"Failed to submit form. Server returned: {response.StatusCode}", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error)
            End If
        Catch ex As Exception
            MessageBox.Show($"An error occurred while submitting the form: {ex.Message}", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error)
        End Try

        ' Store data in MongoDB
        Try
            Dim bsonDocument As BsonDocument = BsonDocument.Parse(jsonContent)
            Await formsCollection.InsertOneAsync(bsonDocument)
            MessageBox.Show("Form data saved to MongoDB.", "Success", MessageBoxButtons.OK, MessageBoxIcon.Information)
        Catch ex As Exception
            MessageBox.Show($"Failed to store form data in MongoDB: {ex.Message}", "MongoDB Error", MessageBoxButtons.OK, MessageBoxIcon.Error)
        End Try
    End Sub

    ' Event handler for Cancel button click
    Private Sub btnCancel_Click(sender As Object, e As EventArgs) Handles btnCancel.Click
        ' Reset form fields or perform any other necessary action
        txtName.Text = ""
        txtEmail.Text = ""
        txtFavoriteColor.Text = ""
        txtFavoriteAnime.Text = ""
        rbGojoYes.Checked = False
        rbGojoNo.Checked = False
        cmbGender.SelectedIndex = -1
        cmbColorOfSky.SelectedIndex = -1
    End Sub
End Class
