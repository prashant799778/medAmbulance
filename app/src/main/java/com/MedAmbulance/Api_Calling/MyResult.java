package com.MedAmbulance.Api_Calling;

import android.location.Location;
import android.os.Bundle;

import com.google.android.gms.common.ConnectionResult;

import org.json.JSONObject;

public interface MyResult  {




    public void onResult(JSONObject object , Boolean status);
}
