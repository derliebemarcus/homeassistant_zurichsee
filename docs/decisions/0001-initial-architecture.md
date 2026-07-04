# 0001: Use a shared update coordinator for station polling.

## Status

Accepted

## Date

2026-07-04

## Context

Home Assistant custom integration for weather-station data around Lake Zurich provided through the tecdottir API.

## Decision drivers

- Reliable weather-data updates
- Correct units and measurement metadata
- Graceful handling of API and station outages

## Considered options

1. Retain the established architecture
2. Replace it with a tightly coupled alternative
3. Defer the architectural boundary to deployment-specific code

## Decision

Use a shared update coordinator for station polling.

## Rationale

A coordinator centralizes API access, update intervals, error handling, and entity availability across all exposed weather measurements.

## Consequences

- The documented building blocks and interfaces remain explicit contracts.
- Changes to the decision require a superseding ADR.

## Risks

- The upstream tecdottir endpoint or payload can change.
- Individual stations can temporarily omit measurements.

## References

- maintenance issue #37
