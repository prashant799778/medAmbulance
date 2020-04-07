package com.example.drivermedambulance.Comman;

import android.text.Editable;
import android.text.TextWatcher;
import android.widget.EditText;

import com.google.android.material.textfield.TextInputEditText;

public class Validation {
    public static Boolean editTextIsFilled(TextInputEditText editText)
    {
        if(editText.length()==0){
            editText.setFocusable(true);
            editText.setError(Constant.PLEASE_FILL_THIS_FIELD);
            return false;
        }
        return true;
    }

    public static Boolean mobileNumberChecker(final EditText editText)
    {
         Boolean status=false;
        editText.addTextChangedListener(new TextWatcher() {
            @Override
            public void beforeTextChanged(CharSequence s, int start, int count, int after) {

            }

            @Override
            public void onTextChanged(CharSequence s, int start, int before, int count) {

            }

            @Override
            public void afterTextChanged(Editable s) {
                if(editText.getText().length()<10)
                {
                    editText.setFocusable(true);
                    editText.setError(Constant.PLEASE_FILL_THIS_FIELD);
                }else if(editText.getText().length()==10)
                    return;
            }
        });
        return true;
    }
}
