package com.example.drivermedambulance.Model;

import java.io.Serializable;

public class EndRideModel implements Serializable {

   String ambulanceLat;
    String ambulanceLng;
     String ambulanceId;
            String bookingId;
             String driverId;
           String dropOff;
           String dropOffLatitude;
            String dropOffLongitude;
            String finalAmount;
            String driverName;
            String userName;

    public String getUserName() {
        return userName;
    }

    public void setUserName(String userName) {
        this.userName = userName;
    }

    public String getDriverName() {
        return driverName;
    }

    public void setDriverName(String driverName) {
        this.driverName = driverName;
    }

    String pickup;
           String status;
           String pickupLatitude;
           String pickupLongitude;
           String totalDistance;
            String userMobile;
           String ambulanceNo;

    public String getAmbulanceLat() {
        return ambulanceLat;
    }

    public void setAmbulanceLat(String ambulanceLat) {
        this.ambulanceLat = ambulanceLat;
    }

    public String getAmbulanceLng() {
        return ambulanceLng;
    }

    public void setAmbulanceLng(String ambulanceLng) {
        this.ambulanceLng = ambulanceLng;
    }

    public String getAmbulanceId() {
        return ambulanceId;
    }

    public void setAmbulanceId(String ambulanceId) {
        this.ambulanceId = ambulanceId;
    }

    public String getBookingId() {
        return bookingId;
    }

    public void setBookingId(String bookingId) {
        this.bookingId = bookingId;
    }

    public String getDriverId() {
        return driverId;
    }

    public void setDriverId(String driverId) {
        this.driverId = driverId;
    }

    public String getDropOff() {
        return dropOff;
    }

    public void setDropOff(String dropOff) {
        this.dropOff = dropOff;
    }

    public String getDropOffLatitude() {
        return dropOffLatitude;
    }

    public void setDropOffLatitude(String dropOffLatitude) {
        this.dropOffLatitude = dropOffLatitude;
    }

    public String getDropOffLongitude() {
        return dropOffLongitude;
    }

    public void setDropOffLongitude(String dropOffLongitude) {
        this.dropOffLongitude = dropOffLongitude;
    }

    public String getFinalAmount() {
        return finalAmount;
    }

    public void setFinalAmount(String finalAmount) {
        this.finalAmount = finalAmount;
    }

    public String getPickup() {
        return pickup;
    }

    public void setPickup(String pickup) {
        this.pickup = pickup;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public String getPickupLatitude() {
        return pickupLatitude;
    }

    public void setPickupLatitude(String pickupLatitude) {
        this.pickupLatitude = pickupLatitude;
    }

    public String getPickupLongitude() {
        return pickupLongitude;
    }

    public void setPickupLongitude(String pickupLongitude) {
        this.pickupLongitude = pickupLongitude;
    }

    public String getTotalDistance() {
        return totalDistance;
    }

    public void setTotalDistance(String totalDistance) {
        this.totalDistance = totalDistance;
    }

    public String getUserMobile() {
        return userMobile;
    }

    public void setUserMobile(String userMobile) {
        this.userMobile = userMobile;
    }

    public String getAmbulanceNo() {
        return ambulanceNo;
    }

    public void setAmbulanceNo(String ambulanceNo) {
        this.ambulanceNo = ambulanceNo;
    }

    public String getDriverMobile() {
        return driverMobile;
    }

    public void setDriverMobile(String driverMobile) {
        this.driverMobile = driverMobile;
    }

    String driverMobile;


}
