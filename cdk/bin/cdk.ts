#!/usr/bin/env node
import "source-map-support/register";
import * as cdk from "aws-cdk-lib";
import { LeyleyStack } from "../lib/leyley-stack";

const app = new cdk.App();

new LeyleyStack(app, "LeyleyStack");
