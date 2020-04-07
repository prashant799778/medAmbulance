package com.example.respondermedambulance.Model;

public class Request {

    String image="";
    String name="";
    String about="";
    String from="";
    String to="";
    String Est_fare="";
    String distance="";
    String distance_from_customer="";
    boolean isAccept;

    public Request() {
    }

    public String getImage() {
        return image;
    }

    public void setImage(String image) {
        this.image = image;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getAbout() {
        return about;
    }

    public void setAbout(String about) {
        this.about = about;
    }

    public String getFrom() {
        return from;
    }

    public void setFrom(String from) {
        this.from = from;
    }

    public String getTo() {
        return to;
    }

    public void setTo(String to) {
        this.to = to;
    }

    public String getEst_fare() {
        return Est_fare;
    }

    public void setEst_fare(String est_fare) {
        Est_fare = est_fare;
    }

    public String getDistance() {
        return distance;
    }

    public void setDistance(String distance) {
        this.distance = distance;
    }

    public String getDistance_from_customer() {
        return distance_from_customer;
    }

    public void setDistance_from_customer(String distance_from_customer) {
        this.distance_from_customer = distance_from_customer;
    }

    public boolean isAccept() {
        return isAccept;
    }

    public void setAccept(boolean accept) {
        isAccept = accept;
    }
}
