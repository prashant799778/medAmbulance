import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { HospitalCurrentBookingComponent } from './hospital-current-booking.component';

describe('HospitalCurrentBookingComponent', () => {
  let component: HospitalCurrentBookingComponent;
  let fixture: ComponentFixture<HospitalCurrentBookingComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ HospitalCurrentBookingComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(HospitalCurrentBookingComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
