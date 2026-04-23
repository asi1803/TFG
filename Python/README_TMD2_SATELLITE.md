# Lectura del archivo TMD2 del satélite

Estos archivos están preparados para el formato real detectado en `SAT_TFG_CASO_01.TMD2`.

## Archivos incluidos

- `tmd2_reader.py`: biblioteca base para abrir y consultar el `.TMD2`
- `extract_satellite_tmd2.py`: exporta tablas CSV
- `plot_satellite_tmd2.py`: dibuja curvas de temperatura u otros atributos
- `requirements_tmd2.txt`: dependencias mínimas

## Dependencias

```bash
pip install -r requirements_tmd2.txt
```

## 1) Ver resumen del archivo

```bash
python tmd2_reader.py SAT_TFG_CASO_01.TMD2
```

## 2) Exportar catálogos de nodos y etiquetas

```bash
python extract_satellite_tmd2.py SAT_TFG_CASO_01.TMD2 --summary --list-labels
```

Esto genera en `output_tmd2/`:
- `nodes_catalog.csv`
- `labels_catalog.csv`

## 3) Exportar temperaturas de un elemento interno

```bash
python extract_satellite_tmd2.py SAT_TFG_CASO_01.TMD2 --label battery_pack --attribute Temperature --csv battery_pack_temperature.csv
```

## 4) Exportar tabla agregada de todos los elementos internos

```bash
python extract_satellite_tmd2.py SAT_TFG_CASO_01.TMD2 --internal-only --all-labels-csv internal_temperatures_mean.csv
```

Las columnas serán:
- adcs_unit
- battery_pack
- body_plate_inf
- body_plate_med
- body_plate_sup
- camera_base
- camera_cyl
- camera_electronics
- camera_lens
- comms_box
- obc_box

El índice es el tiempo en segundos.

## 5) Dibujar temperaturas

```bash
python plot_satellite_tmd2.py SAT_TFG_CASO_01.TMD2 --label battery_pack --time-unit h
```

Comparación entre varios subsistemas:

```bash
python plot_satellite_tmd2.py SAT_TFG_CASO_01.TMD2 --label battery_pack --label obc_box --label comms_box --time-unit h
```

## 6) Representar nodos concretos

```bash
python plot_satellite_tmd2.py SAT_TFG_CASO_01.TMD2 --nodes 10000 10001 10002 --time-unit h
```

## Atributos disponibles en tu archivo

- Temperature
- Capacitance
- Total_Albedo_Heat_Source
- Total_Earth_Heat_Source
- Total_Internal_Heat_Source
- Total_Rest_Heat_Source
- Total_Solar_Heat_Source
- Area
- Solar_Absorptivity
- Infra-Red_Emissivity
- Incident_Albedo_Heat_Source
- Incident_Earth_Heat_Source
- Incident_Solar_Heat_Source
- X_Coordinate
- Y_Coordinate
- Z_Coordinate

## Etiquetas detectadas en tu satélite

- BODY_PANEL_EXT
- BODY_PANEL_INT
- ENVIRONMENT
- INACTIVE_NODE
- MLI_EXT
- MLI_INT
- STR_AV_RAD
- adcs_unit
- battery_pack
- body_plate_inf
- body_plate_med
- body_plate_sup
- camera_base
- camera_cyl
- camera_electronics
- camera_lens
- comms_box
- obc_box
- radiator
- solar_panel_1
- solar_panel_2
