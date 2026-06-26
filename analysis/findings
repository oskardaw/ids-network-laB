# Findings and Results

## General Observations

The conducted experiments demonstrated significant differences in how Snort, Suricata, and Zeek interpret and report network activity under identical conditions.

Although all systems operated on the same traffic dataset, their detection approaches and output formats varied considerably.

## Detection Behavior Comparison

### Snort
- Focused primarily on signature-based detection
- Generated clear and structured alerts for predefined patterns
- Limited visibility into contextual network behavior
- Effective for known attack signatures, less flexible for unknown patterns

### Suricata
- Similar signature-based detection model as Snort
- Provided more detailed and verbose alert output
- Better performance in high-volume traffic scenarios
- More informative logs for post-analysis

### Zeek
- Operated on event-based analysis rather than signature matching
- Did not generate traditional intrusion alerts
- Provided deep visibility into network behavior through logs (e.g., conn.log, icmp.log)
- Most useful for behavioral analysis and forensic investigation

## Key Findings

- Signature-based systems (Snort, Suricata) are effective for detecting known attack patterns but depend heavily on rule quality.
- Zeek provides better situational awareness but requires manual analysis of logs.
- High traffic scenarios (e.g., UDP flood simulation) generated increased noise and false positives in all systems.
- Proper tuning of detection rules significantly impacts accuracy and noise reduction.

## Conclusion

Each system serves a different purpose in a security monitoring environment:

- Snort: lightweight and rule-focused detection
- Suricata: enhanced performance and richer alerts
- Zeek: advanced network behavior analysis and forensic capabilities

The results suggest that combining signature-based and behavior-based tools provides the most complete visibility in network security monitoring environments.
