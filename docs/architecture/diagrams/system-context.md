# System context diagram

```mermaid
flowchart LR
    User["User or operator"] --> Project["Zürichsee Wetterstationen Home Assistant Integration"]
    External1["Home Assistant"]
    External2["tecdottir API"]
    External3["Wasserschutzpolizei Zurich weather stations"]
    External4["HACS and GitHub Releases"]
    External5["Jenkins, SonarQube, Coveralls, and security scanners"]
    Project --> External1
```
