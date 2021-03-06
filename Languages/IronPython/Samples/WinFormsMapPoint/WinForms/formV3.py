##############################################################################
#
#  Copyright (c) Microsoft Corporation. All rights reserved.
#
# This source code is subject to terms and conditions of the Apache License,
# Version 2.0. A copy of the license can be found in the License.html file at
# the root of this distribution. If you cannot locate the  Apache License,
# Version 2.0, please send an email to ironpy@microsoft.com. By using this
# source code in any fashion, you are agreeing to be bound by the terms of
# the Apache License, Version 2.0.
#
# You must not remove this notice, or any other, from this software.
#
#
##############################################################################

import clr
clr.AddReference("System.Windows.Forms")

from System.Windows.Forms import *


class FormV3(Form):
    def __init__(self):
        self.Text = "Hello World (" + __file__ + ")"

        # Create Label
        self.Controls.Add(Label(Text="Enter Message:"))

        # Create TextBox
        self._txtMessage = TextBox(Left=100)
        self.Controls.Add(self._txtMessage)

        # Create Button
        msgButton = Button(Text="Message", Left=20, Top=25)
        msgButton.Click += self.OnMsgButtonClick
        self.Controls.Add(msgButton)

    def OnMsgButtonClick(self, *args):
        MessageBox.Show(self._txtMessage.Text, "Message")

Application.Run(FormV3())
