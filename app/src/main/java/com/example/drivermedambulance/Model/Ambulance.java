package com.example.drivermedambulance.Model;

public class Ambulance {
    String ambId;
    String  ambNo;
     String distance;
     String lat;
     String lng;
     String  mobileNo;
     String driverName;

    public Ambulance() {
    }

    public Ambulance(String ambId, String ambNo, String distance, String lat, String lng, String mobileNo, String driverName) {
        this.ambId = ambId;
        this.ambNo = ambNo;
        this.distance = distance;
        this.lat = lat;
        this.lng = lng;
        this.mobileNo = mobileNo;
        this.driverName = driverName;
    }

    public String getAmbId() {
        return ambId;
    }

    public void setAmbId(String ambId) {
        this.ambId = ambId;
    }

    public String getAmbNo() {
        return ambNo;
    }

    public void setAmbNo(String ambNo) {
        this.ambNo = ambNo;
    }

    public String getDistance() {
        return distance;
    }

    public void setDistance(String distance) {
        this.distance = distance;
    }

    public String getLat() {
        return lat;
    }

    public void setLat(String lat) {
        this.lat = lat;
    }

    public String getLng() {
        return lng;
    }

    public void setLng(String lng) {
        this.lng = lng;
    }

    public String getMobileNo() {
        return mobileNo;
    }

    public void setMobileNo(String mobileNo) {
        this.mobileNo = mobileNo;
    }

    public String getDriverName() {
        return driverName;
    }

    public void setDriverName(String driverName) {
        this.driverName = driverName;
    }
}
