package com.MedAmbulance.Model;

public class RateCardModel {
    String ambType;
    String category;
    String farePerKM;
    String minDistance;
    String minFare;
    String waitFare;

    public String getAmbType() {
        return ambType;
    }

    public void setAmbType(String ambType) {
        this.ambType = ambType;
    }

    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
    }

    public String getFarePerKM() {
        return farePerKM;
    }

    public void setFarePerKM(String farePerKM) {
        this.farePerKM = farePerKM;
    }

    public String getMinDistance() {
        return minDistance;
    }

    public void setMinDistance(String minDistance) {
        this.minDistance = minDistance;
    }

    public String getMinFare() {
        return minFare;
    }

    public void setMinFare(String minFare) {
        this.minFare = minFare;
    }

    public String getWaitFare() {
        return waitFare;
    }

    public void setWaitFare(String waitFare) {
        this.waitFare = waitFare;
    }
}
