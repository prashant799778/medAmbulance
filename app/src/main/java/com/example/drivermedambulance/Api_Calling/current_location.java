package com.example.drivermedambulance.Api_Calling;

import android.location.Location;
import android.os.Bundle;

import com.google.android.gms.common.ConnectionResult;

public interface current_location {

    void onConnected(Bundle bundle);

    void onLocationChanged(Location location);

    void onConnectionFailed(ConnectionResult connectionResult);
}
