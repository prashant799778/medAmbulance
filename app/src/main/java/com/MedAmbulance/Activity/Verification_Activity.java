package com.MedAmbulance.Activity;

import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;

import android.app.Dialog;
import android.content.DialogInterface;
import android.content.Intent;
import android.graphics.Rect;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.view.Window;
import android.widget.Button;

import com.MedAmbulance.R;
import com.MedAmbulance.Widget.OtpEditText;
import com.google.android.material.dialog.MaterialAlertDialogBuilder;

public class Verification_Activity extends AppCompatActivity {
     OtpEditText otpEditText;
     Button done;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_verification_);
        otpEditText=findViewById(R.id.et_otp);
        done=findViewById(R.id.done);
        done.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
//             startActivity(new Intent(Verification_Activity.this,Driver_Registration.class));
                Rect displayRectangle = new Rect();
                Window window = Verification_Activity.this.getWindow();
                window.getDecorView().getWindowVisibleDisplayFrame(displayRectangle);
                final MaterialAlertDialogBuilder alertDialogBuilder=new MaterialAlertDialogBuilder(Verification_Activity.this,R.style.custom_dialog);
                final AlertDialog alertDialog = alertDialogBuilder.create();
                alertDialogBuilder.setMessage(getResources().getString(R.string.doneText));
                final View dialogView = LayoutInflater.from(v.getContext()).inflate(R.layout.custom_dialog, null, false);
                Button ok=dialogView.findViewById(R.id.buttonOk);
                alertDialog.setView(dialogView);
                alertDialog.show();
                ok.setOnClickListener(new View.OnClickListener() {
                    @Override
                    public void onClick(View v) {
                        startActivity(new Intent(Verification_Activity.this,Driver_Registration.class));
                        alertDialog.dismiss();
                    }
                });
            }
        });
    }
}
