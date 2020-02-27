import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { HospitalAccountComponent } from './hospital-account.component';

describe('HospitalAccountComponent', () => {
  let component: HospitalAccountComponent;
  let fixture: ComponentFixture<HospitalAccountComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ HospitalAccountComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(HospitalAccountComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
