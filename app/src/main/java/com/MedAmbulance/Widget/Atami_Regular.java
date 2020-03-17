package com.MedAmbulance.Widget;

import android.annotation.SuppressLint;
import android.content.Context;
import android.graphics.Canvas;
import android.graphics.Typeface;
import android.util.AttributeSet;
import android.widget.TextView;

@SuppressLint("AppCompatCustomView")
public class Atami_Regular extends TextView {


    public Atami_Regular(Context context) {
        super(context);
        Typeface face= Typeface.createFromAsset(context.getAssets(), "AtamiRegular.otf");
        this.setTypeface(face);
    }

    public Atami_Regular(Context context, AttributeSet attrs) {
        super(context, attrs);
        Typeface face=Typeface.createFromAsset(context.getAssets(), "AtamiRegular.otf");
        this.setTypeface(face);
    }

    public Atami_Regular(Context context, AttributeSet attrs, int defStyle) {
        super(context, attrs, defStyle);
        Typeface face=Typeface.createFromAsset(context.getAssets(), "AtamiRegular.otf");
        this.setTypeface(face);
    }

    protected void onDraw (Canvas canvas) {
        super.onDraw(canvas);

    }

}
