Public Class frmDSKY

    ' Global Variables
    ' Verb
    Dim verbEntryActive As Boolean = False
    Dim remainingVerbChars As Integer = 2
    Dim currentVerb As String = "00"

    ' Noun
    Dim nounEntryActive As Boolean = False
    Dim remainingNounChars As Integer = 2
    Dim currentNoun As String = "00"

    ' AGC States
    Dim inComputerActivity As Boolean = False
    Dim inUplinkActivity As Boolean = False
    Dim inTemperature As Boolean = False
    Dim inNoAttitude As Boolean = False
    Dim inGimbalLock As Boolean = False
    Dim inStandby As Boolean = False
    Dim inProgram As Boolean = False
    Dim inKeyRelease As Boolean = False
    Dim inRestart As Boolean = False
    Dim inOperatorError As Boolean = False
    Dim inTracker As Boolean = False
    Dim inTestMode As Boolean = False

    Private Sub btnVerb_Click(sender As Object, e As EventArgs) Handles btnVerb.Click
        If (Not verbEntryActive And Not nounEntryActive) Then
            verbEntryActive = True
            Return

        End If

        inOperatorError = True

    End Sub

    Private Sub btnNoun_Click(sender As Object, e As EventArgs) Handles btnNoun.Click

        If (verbEntryActive And Not nounEntryActive) Then
            verbEntryActive = False
            nounEntryActive = True
            Return
        End If

        inOperatorError = True
    End Sub

    Private Sub btnEnter_Click(sender As Object, e As EventArgs) Handles btnEnter.Click

        ' Full Command Entered
        If (Not verbEntryActive And nounEntryActive) Then
            verbEntryActive = False
            nounEntryActive = False

            indVerb.BackColor = Control.DefaultBackColor
            indNoun.BackColor = Control.DefaultBackColor

            disVerb.Visible = True
            disNoun.Visible = True

        End If

        ' Reset variables
        remainingVerbChars = 2
        remainingNounChars = 2

        ' Execute the 
        PerformAction()


    End Sub

    Private Sub btnNumeric_Click(sender As Object, e As EventArgs) Handles btnOne.Click, btnTwo.Click, btnThree.Click, btnFour.Click, btnFive.Click, btnSix.Click, btnSeven.Click, btnEight.Click, btnNine.Click, btnZero.Click

        If (verbEntryActive And Not nounEntryActive) Then
            If (remainingVerbChars = 2) Then
                currentVerb = sender.Text + "0"
            ElseIf (remainingVerbChars = 1) Then
                currentVerb = Strings.GetChar(currentVerb, 1) + sender.Text
            End If

            remainingVerbChars -= 1

        End If

        If (nounEntryActive And Not verbEntryActive) Then
            If (remainingNounChars = 2) Then
                currentNoun = sender.Text + "0"
            ElseIf (remainingNounChars = 1) Then
                currentNoun = Strings.GetChar(currentNoun, 1) + sender.Text
            End If

            remainingNounChars -= 1

        End If

        If ((nounEntryActive And verbEntryActive) Or (Not nounEntryActive And Not verbEntryActive)) Then
            inOperatorError = True
        End If

    End Sub

    Private Sub PerformAction()

        Dim validCommand As Boolean = CommandLookup(currentVerb, currentNoun)

    End Sub

    Private Function CommandLookup(ByVal verb As String, ByVal noun As String)

        Select Case verb + noun
            Case "9999"
                TestMode()
                Return True
        End Select

        inOperatorError = True
        Return False

    End Function

    Private Sub Command01()

    End Sub

    Private Sub TestMode()
        inComputerActivity = True
        inUplinkActivity = True
        inTemperature = True
        inNoAttitude = True
        inGimbalLock = True
        inStandby = True
        inProgram = True
        inKeyRelease = True
        inRestart = True
        inOperatorError = True
        inTracker = True

        inTestMode = True
    End Sub

    Private Sub SetDisplay()
        If (verbEntryActive) Then
            disVerb.Visible = Not disVerb.Visible
            disVerb.Text = currentVerb

            indVerb.BackColor = Color.Green
            lblVerb.ForeColor = Color.White
        Else
            disVerb.Visible = True
            disVerb.Text = currentVerb

            indVerb.BackColor = Control.DefaultBackColor
            lblVerb.ForeColor = Color.Black
        End If

        If (nounEntryActive) Then
            disNoun.Visible = Not disNoun.Visible
            disNoun.Text = currentNoun

            indNoun.BackColor = Color.Green
            lblNoun.ForeColor = Color.White
        Else
            disNoun.Visible = True
            disNoun.Text = currentNoun

            indNoun.BackColor = Control.DefaultBackColor
            lblNoun.ForeColor = Color.Black

        End If

        If (inComputerActivity) Then
            If (indComputerActivity.BackColor = Control.DefaultBackColor) Then
                indComputerActivity.BackColor = Color.Yellow
            Else
                indComputerActivity.BackColor = Control.DefaultBackColor
            End If
        Else
            indComputerActivity.BackColor = Control.DefaultBackColor
        End If

        If (inUplinkActivity) Then
            If (indUplinkActivity.BackColor = Control.DefaultBackColor) Then
                indUplinkActivity.BackColor = Color.Green
            Else
                indUplinkActivity.BackColor = Control.DefaultBackColor
            End If
        Else
            indUplinkActivity.BackColor = Control.DefaultBackColor
        End If

        If (inTemperature) Then
            If (indTemperature.BackColor = Control.DefaultBackColor) Then
                indTemperature.BackColor = Color.Red
                lblTemperature.ForeColor = Color.White
            Else
                indTemperature.BackColor = Control.DefaultBackColor
                lblTemperature.ForeColor = Color.Black
            End If
        Else
            indTemperature.BackColor = Control.DefaultBackColor
            lblTemperature.ForeColor = Color.Black
        End If

        If (inNoAttitude) Then
            If (indNoAttitude.BackColor = Control.DefaultBackColor) Then
                indNoAttitude.BackColor = Color.Red
                lblNoAttitude.ForeColor = Color.White
            Else
                indNoAttitude.BackColor = Control.DefaultBackColor
                lblNoAttitude.ForeColor = Color.Black
            End If
        Else
            indNoAttitude.BackColor = Control.DefaultBackColor
            lblNoAttitude.ForeColor = Color.Black
        End If

        If (inGimbalLock) Then
            If (indGimbalLock.BackColor = Control.DefaultBackColor) Then
                indGimbalLock.BackColor = Color.Red
                lblGimbalLock.ForeColor = Color.White
            Else
                indGimbalLock.BackColor = Control.DefaultBackColor
                lblGimbalLock.ForeColor = Color.Black
            End If
        Else
            indGimbalLock.BackColor = Control.DefaultBackColor
            lblGimbalLock.ForeColor = Color.Black
        End If

        If (inStandby) Then
            If (indStandby.BackColor = Control.DefaultBackColor) Then
                indStandby.BackColor = Color.Yellow
            Else
                indStandby.BackColor = Control.DefaultBackColor
            End If
        Else
            indStandby.BackColor = Control.DefaultBackColor
        End If

        If (inProgram) Then
            If (indProgramActivity.BackColor = Control.DefaultBackColor) Then
                indProgramActivity.BackColor = Color.Yellow
            Else
                indProgramActivity.BackColor = Control.DefaultBackColor
            End If
        Else
            indProgramActivity.BackColor = Control.DefaultBackColor
        End If

        If (inKeyRelease) Then
            If (indKeyRelease.BackColor = Control.DefaultBackColor) Then
                indKeyRelease.BackColor = Color.Yellow
            Else
                indKeyRelease.BackColor = Control.DefaultBackColor
            End If
        Else
            indKeyRelease.BackColor = Control.DefaultBackColor
        End If

        If (inRestart) Then
            If (indRestart.BackColor = Control.DefaultBackColor) Then
                indRestart.BackColor = Color.Yellow
            Else
                indRestart.BackColor = Control.DefaultBackColor
            End If
        Else
            indRestart.BackColor = Control.DefaultBackColor
        End If

        If (inOperatorError And inTestMode) Then
            If (indOperatorError.BackColor = Control.DefaultBackColor) Then
                indOperatorError.BackColor = Color.Red
                lblOperatorError.ForeColor = Color.White
            Else
                indOperatorError.BackColor = Control.DefaultBackColor
                lblOperatorError.ForeColor = Color.Black
            End If
        Else
            indOperatorError.BackColor = Control.DefaultBackColor
        End If

        If (inTracker) Then
            If (indTracker.BackColor = Control.DefaultBackColor) Then
                indTracker.BackColor = Color.Yellow
            Else
                indTracker.BackColor = Control.DefaultBackColor
            End If
        Else
            indTracker.BackColor = Control.DefaultBackColor
        End If

    End Sub

    Private Sub ResetComputer()
        ' AGC State Reset
        inComputerActivity = False
        inUplinkActivity = False
        inTemperature = False
        inNoAttitude = False
        inGimbalLock = False
        inStandby = False
        inProgram = False
        inKeyRelease = False
        inRestart = False
        inOperatorError = False
        inTracker = False
        inTestMode = False

        ' Verb Reset
        currentVerb = "00"
        verbEntryActive = False
        remainingVerbChars = 2

        ' Noun Reset
        currentNoun = "00"
        nounEntryActive = False
        remainingNounChars = 2

    End Sub

    Private Sub btnReset_Click(sender As Object, e As EventArgs) Handles btnReset.Click
        ResetComputer()
    End Sub

    Private Sub tmrAGCClock_Tick(sender As Object, e As EventArgs) Handles tmrAGCClock.Tick
        SetDisplay()
    End Sub

    Private Sub tmrRapidUpdate_Tick(sender As Object, e As EventArgs) Handles tmrRapidUpdate.Tick
        If (Not inOperatorError And Not inTestMode) Then
            indOperatorError.BackColor = Control.DefaultBackColor
            lblOperatorError.ForeColor = Color.Black
        End If

        If (inOperatorError And Not inTestMode) Then
            If (inOperatorError) Then
                If (indOperatorError.BackColor = Control.DefaultBackColor) Then
                    indOperatorError.BackColor = Color.Red
                    lblOperatorError.ForeColor = Color.White
                Else
                    indOperatorError.BackColor = Control.DefaultBackColor
                    lblOperatorError.ForeColor = Color.Black
                End If
            End If
        End If

    End Sub
End Class
