terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "3.5.0"
    }
  }
}

provider "google" {
  credentials = file("./assignment-2-389700-399d157e6a98.json")
  project     = "assignment-2-389700"
  region      = "us-central1-a"
}

resource "google_container_cluster" "cluster" {
  name               = "cluster-1"
  location           = "us-central1-a"
  initial_node_count = 1

  node_config {
    machine_type = "e2-micro"
    disk_type    = "pd-standard"
    disk_size_gb = 10
    image_type   = "COS_CONTAINERD"
  }
}